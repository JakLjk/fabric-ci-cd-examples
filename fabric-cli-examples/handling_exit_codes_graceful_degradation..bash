# Continue execution even if optional commands fail
# Works only in BASH CLI ( || conditional operatior is bash syntax)
fab get OptionalItem.Notebook || echo "Optional item not found, continuing..."