variable "account_id" {
  type        = string
  description = "Cloudflare account identifier, supplied outside Git."
  validation {
    condition     = can(regex("^[a-f0-9]{32}$", var.account_id))
    error_message = "Use a 32-character hexadecimal account identifier."
  }
}

variable "existing_site_id" {
  type        = string
  description = "Existing Web Analytics site identifier, supplied outside Git."
  validation {
    condition     = can(regex("^[a-f0-9]{32}$", var.existing_site_id))
    error_message = "Use the existing 32-character hexadecimal site identifier."
  }
}
