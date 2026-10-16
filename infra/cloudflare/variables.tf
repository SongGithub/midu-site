variable "zone_id" {
  description = "Shared midu.com.au zone ID, owned by personal-infra."
  type        = string
  validation {
    condition     = can(regex("^[a-f0-9]{32}$", var.zone_id))
    error_message = "Use the existing 32-character Cloudflare zone ID."
  }
}

variable "existing_dns" {
  description = "Existing www and blog DNS record IDs for adoption."
  type        = object({ www = string, blog = string })
}
