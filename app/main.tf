provider "aws" {
  region = "us-east-1"
}

# ❌ Public S3 bucket
resource "aws_s3_bucket" "bad_bucket" {
  bucket = "my-public-bucket-12345"
  acl    = "public-read"
}

# ❌ Security group open to internet
resource "aws_security_group" "bad_sg" {
  name = "bad-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # SSH open to world
  }
}

# ❌ Hardcoded secret
variable "db_password" {
  default = "SuperSecret123"
}

# ❌ Unencrypted storage
resource "aws_ebs_volume" "bad_volume" {
  availability_zone = "us-east-1a"
  size              = 10
  encrypted         = false
}
