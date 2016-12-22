# servicerocket-workplace-examples

Collection of examples using the API of Workplace by Facebook.

## Run

Run with `python`, see docstring of each file.

    pip install -r requirements.txt
    python <script> <args>

Or with `docker`, e.g. for `post-to-group.py`:

    docker build -t workplace-examples .
    docker run -it --rm -v "$PWD:/app" -w /app -e ACCESS_TOKEN=$ACCESS_TOKEN -e COMMUNITY_ID=$COMMUNITY_ID workplace-examples post-to-group.py <user> <group> "Hello world!"
