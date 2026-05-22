resource "aws_db_instance" "staging_db" {
  identifier             = "staging-db"
  allocated_storage      = 100
  engine                 = "mysql"
  engine_version         = "8.0"
  instance_class         = "db.m5.large"
  username               = "adminuser"
  password               = "Password123!"
  publicly_accessible    = false
  skip_final_snapshot    = true
  backup_retention_period = 0

  tags = {
    Environment = "staging"
  }
}