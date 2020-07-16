variable "server_port" {
  type = number
  description = "Server port"
  default = 8000
}

variable "app" {
  type = string
  description = "Application"
  default = "bay-area-relief"
}

variable "env" {
  type = string
  description = "Environment"
  default = "dev"
}

variable "region" {
  type = string
  description = "AWS Region"
  default = "us-west-1"
}

variable "profile" {
  type = string
  description = "AWS Profile"
  default = "codesf"
}

variable "database_name" {
  type = string
  description = "Database name"
  default = "bar"
}

variable "db_azs" {
  type = list(string)
  description = "Database name"
  default = ["us-west-1a"]
}

variable "instance_type" {
  type = string
  description = "EC2 Instance type"
  default =  "t2.micro"
}

variable "db_instance_type" {
  type = string
  description = "RDS Instance type"
  default =  "db.t2.micro"
}

variable "db_username" {
  type = string
  description = "Database username"
}

variable "db_password" {
  type = string
  description = "Database password"
}