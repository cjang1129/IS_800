terraform {
  backend "s3" {
    bucket         = "cj-is800-lab7a"
    key            = "terraform/state.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}

resource "aws_instance" "example" {
  ami           = "ami-08b5b3a93ed654d19"
  instance_type = "t2.micro"
  tags = {
    Name = "Terraform-Test-Instance"
  }
}
