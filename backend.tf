terraform {
  backend "s3" {
    bucket         = "suyash-terraform-state-cb8ee023"
    key            = "dev/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-lock-table"
    encrypt        = true
  }
}