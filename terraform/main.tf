provider "aws" {
  region = var.region
  profile = var.profile
}

resource "tls_private_key" "server" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "generated_key" {
  key_name   = "${var.app}-key"
  public_key = tls_private_key.server.public_key_openssh
}


resource "aws_launch_template" "server" {
  name_prefix = var.app
  image_id      = data.aws_ami.ubuntu.id
  instance_type = var.instance_type
  user_data     =  base64encode(data.template_file.user_data.rendered)

  block_device_mappings {
    device_name = "/dev/sda1"

    ebs {
      encrypted   = true
      volume_type = "gp2"
      volume_size = "10"
    }
  }

  vpc_security_group_ids = concat([aws_security_group.http.id, aws_security_group.bastion.id])

  tags = {
    Name = var.app
  }

  tag_specifications {
    resource_type = "instance"

    tags = {
      Name = var.app
    }
  }

  key_name = aws_key_pair.generated_key.key_name
}


resource "aws_autoscaling_group" "server" {
  name_prefix         = var.app
  availability_zones = var.db_azs
  desired_capacity    =  1
  min_size             = 1
  max_size             = 2

  launch_template {
    id      = aws_launch_template.server.id
    version = "$Latest"
  }

}
