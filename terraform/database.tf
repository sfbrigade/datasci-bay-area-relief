resource "aws_security_group" "postgresql" {
  name        = "postgres"
  description = "postgres"
  vpc_id      = aws_default_vpc.default.id

  ingress {
    description = "TLS from VPC"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "postgres"
  }
}


resource "aws_db_instance" "postgresql" {
  allocated_storage    = 10
  storage_type         = "gp2"
  engine               = "postgres"
  identifier           = var.app
  engine_version       = "11.6"
  instance_class       = var.db_instance_type
  name                 = "bar"
  username             = var.db_username
  password             = var.db_password
  final_snapshot_identifier = var.app
  publicly_accessible  = true
  vpc_security_group_ids = concat([aws_security_group.postgresql.id])
}