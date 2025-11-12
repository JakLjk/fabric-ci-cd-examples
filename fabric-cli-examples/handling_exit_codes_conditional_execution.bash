# Retry authentication on failure
for i in {1..3}; do
    if fab auth status; then
        break
    elif [ $? -eq 4 ]; then
        echo "Attempt $i: Re-authenticating..."
        fab auth login
    else
        echo "Authentication check failed"
        exit 1
    fi
done