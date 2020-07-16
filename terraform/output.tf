output "private_pem" {
  value = tls_private_key.server.private_key_pem
}

output "public_pem" {
  value = tls_private_key.server.public_key_pem
}

output "public_key_openssh" {
  value = tls_private_key.server.public_key_openssh
}
