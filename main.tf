

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "demo_bucket" {
  bucket = "suyash-demo-${random_id.bucket_suffix.hex}"

  tags = {
    Name        = "DemoBucket"
    Environment = "Dev"
  }
}