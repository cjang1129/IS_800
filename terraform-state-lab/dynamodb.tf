resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "Users"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "UserId"
  range_key      = "UserName"

  attribute {
    name = "UserId"
    type = "S"
  }

  attribute {
    name = "UserName"
    type = "S"
  }

}