provider "aws" {
  region = "us-east-2"
}

module "kms_key" {
  source = "cloudposse/kms-key/aws"

  namespace               = "org_name"
  name                    = "xxx_solution_name"

  # Duration in days till which the scheduled deletion can be cancelled
  # once destruction of the resource is initiated from the console Takes value between 7-30 days
  deletion_window_in_days = 30

  # Always set this to false
  enable_key_rotation     = false

  # Should start with alias; Displayed on AWS Console
  alias                   = "alias/xxx-pool-harvest-signer"
  description             = "Some long description"

  key_usage               = "SIGN_VERIFY"
  customer_master_key_spec= "ECC_SECG_P256K1"

  context = module.this.context
}
