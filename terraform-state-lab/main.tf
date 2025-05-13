provider "aws" {
  region = "us-east-1"  # Modify region if needed
}

resource "aws_instance" "my_ec2" {
  ami           = "ami-08b5b3a93ed654d19"  # Replace with a valid AMI ID
  instance_type = "t2.micro"
  key_name      = "firstkey"  # Replace with an existing AWS key pair
  tags = {
    Name = "i-00246f09e11b3f7a1"  # Modify instance name
  }
}
