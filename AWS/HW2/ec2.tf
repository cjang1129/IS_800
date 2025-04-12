module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"

  name = "single-instance"

  instance_type          = "t2.micro"
  key_name               = "firstkey"
  monitoring             = true
  vpc_security_group_ids = ["sg-0ad09eab55a727533"]
  subnet_id              = "subnet-0a9278facbb19dcb6"
}