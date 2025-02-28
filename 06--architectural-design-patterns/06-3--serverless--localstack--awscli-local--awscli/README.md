# Architectural Desing Patterns

## Serverless

The *Serverless* pattern abstracts server management, allowing developers to focus solely on code.
Cloud providers handle the scaling and execution based on event triggers, 
such as HTTP requests, file uploads, or database modifications.
For example, AWS Lambda is Amazon's serverless compute service, which runs code in response to triggers.

### Example: using AWS Lambda to square a number

- AWS Lambda is Amazon's serverless compute service, which runs code in response to triggers.

- For this example, we need the virtual environment with Python 3.11 and
    
  - **Docker**
    
    ```unix
    $ docker --version
    Docker version 27.1.2, build d01f264
    
    $ sudo update-alternatives --config python3
    Es gibt 2 Auswahlmöglichkeiten für die Alternative python3 (welche /usr/bin/python3 bereitstellen).
    
      Auswahl      Pfad                 Priorität Status
    ------------------------------------------------------------
    * 0            /usr/bin/python3.11   2         automatischer Modus
      1            /usr/bin/python3.10   1         manueller Modus
      2            /usr/bin/python3.11   2         manueller Modus
    
    Drücken Sie die Eingabetaste, um die aktuelle Wahl[*] beizubehalten,
    oder geben Sie die Auswahlnummer ein: 1
    update-alternatives: /usr/bin/python3.10 wird verwendet, um /usr/bin/python3 (python3) im manuellen Modus bereitzustellen
    
    $ sudo apt-get update
    OK:2 http://de.archive.ubuntu.com/ubuntu jammy InRelease
    Ign:3 https://pkg.jenkins.io/debian-stable binary/ InRelease
    OK:4 http://de.archive.ubuntu.com/ubuntu jammy-updates InRelease
    OK:5 https://pkg.jenkins.io/debian-stable binary/ Release
    OK:6 https://download.docker.com/linux/ubuntu jammy InRelease
    OK:7 http://de.archive.ubuntu.com/ubuntu jammy-backports InRelease
    OK:8 https://dl.google.com/linux/chrome/deb stable InRelease
    OK:9 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu jammy InRelease
    OK:1 https://packages.microsoft.com/repos/code stable InRelease
    OK:10 http://security.ubuntu.com/ubuntu jammy-security InRelease
    Paketlisten werden gelesen… Fertig
    
    $ sudo apt-get install --only-upgrade docker-ce docker-ce-cli containerd.io
    Paketlisten werden gelesen… Fertig
    Abhängigkeitsbaum wird aufgebaut… Fertig
    Statusinformationen werden eingelesen… Fertig
    Das folgende Paket wurde automatisch installiert und wird nicht mehr benötigt:
      python3-wheel
    Verwenden Sie »sudo apt autoremove«, um es zu entfernen.
    Vorgeschlagene Pakete:
      cgroupfs-mount | cgroup-lite
    Die folgenden Pakete werden aktualisiert (Upgrade):
      containerd.io docker-ce docker-ce-cli
    3 aktualisiert, 0 neu installiert, 0 zu entfernen und 285 nicht aktualisiert.
    Es müssen 64,5 MB an Archiven heruntergeladen werden.
    Nach dieser Operation werden 18,7 MB Plattenplatz freigegeben.
    Holen:1 https://download.docker.com/linux/ubuntu jammy/stable amd64 containerd.io amd64 1.7.25-1 [29,6 MB]
    Holen:2 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce-cli amd64 5:28.0.0-1~ubuntu.22.04~jammy [15,7 MB]
    Holen:3 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce amd64 5:28.0.0-1~ubuntu.22.04~jammy [19,1 MB]
    Es wurden 64,5 MB in 2 s geholt (34,4 MB/s).
    (Lese Datenbank ... 267782 Dateien und Verzeichnisse sind derzeit installiert.)
    Vorbereitung zum Entpacken von .../containerd.io_1.7.25-1_amd64.deb ...
    Entpacken von containerd.io (1.7.25-1) über (1.7.20-1) ...
    Vorbereitung zum Entpacken von .../docker-ce-cli_5%3a28.0.0-1~ubuntu.22.04~jammy_amd64.deb ...
    Entpacken von docker-ce-cli (5:28.0.0-1~ubuntu.22.04~jammy) über (5:27.1.2-1~ubuntu.22.04~jammy) ...
    Vorbereitung zum Entpacken von .../docker-ce_5%3a28.0.0-1~ubuntu.22.04~jammy_amd64.deb ...
    Entpacken von docker-ce (5:28.0.0-1~ubuntu.22.04~jammy) über (5:27.1.2-1~ubuntu.22.04~jammy) ...
    containerd.io (1.7.25-1) wird eingerichtet ...
    docker-ce-cli (5:28.0.0-1~ubuntu.22.04~jammy) wird eingerichtet ...
    docker-ce (5:28.0.0-1~ubuntu.22.04~jammy) wird eingerichtet ...
    Trigger für man-db (2.10.2-1) werden verarbeitet ...
    
    $ docker --version
    Docker version 28.0.0, build f9ced58
    
    $ whoami
    <username>
    
    $ sudo usermod -aG docker <username>
    $ gnome-session-quit --no-prompt
    $ id -nG
    <username> adm cdrom sudo dip plugdev lpadmin lxd sambashare docker
    ```
    
  - **LocalStack** (cloud service emulator that runs in a single container on your laptop or in your CI environment)
  for testing AWS Lambda locally:
    
    - https://pypi.org/project/localstack/
    - https://github.com/localstack/localstack
    - https://snyk.io/advisor/python/localstack
    
    ```unix
    $ python -m pip install localstack
    ```
    
  - **awscli-local** (to deploy the Lambda function into the "local stack" AWS infrastructure)
    
    - https://pypi.org/project/awscli-local/
    - https://github.com/localstack/awscli-local
    - https://snyk.io/advisor/python/awscli-local
    
    ```unix
    $ python -m pip install awscli-local
    ```
    
  - **awscli**
    
    - https://pypi.org/project/awscli/
    - https://github.com/aws/aws-cli
    - https://snyk.io/advisor/python/awscli
    
    ```unix
    $ python -m pip install awscli
    ```

- Map the domain name `localhost.localstack.cloud` to the local machine
  ```unix
  $ sudo nano /etc/hosts
  ```
  Add `127.0.0.1   localhost.localstack.cloud`, then `Ctrl+O`, `Enter`, `Ctrl+X`.

- Stop and disable `systemd-resolved`
  ```unix
  $ sudo systemctl stop systemd-resolved
  $ sudo systemctl disable systemd-resolved
  ```
  
- Update DNS configuration
  ```unix
  $ sudo nano /etc/resolv.conf
  ```
  Update to
  ```
  nameserver 8.8.8.8
  nameserver 8.8.4.4
  ```

- Restart the `systemd-networkd` service
  ```unix
  $ sudo systemctl restart systemd-networkd
  ```

- Start LocalStack inside a Docker container by running the available executable in the Python environment
    ```unix
    $ docker run -d --name localstack \
      -p 4566:4566 \
      -p 53:53 \
      -p 53:53/udp \
      -e DNS_ADDRESS=0.0.0.0 \
      -e SERVICES=lambda \
      -v /var/run/docker.sock:/var/run/docker.sock \
      localstack/localstack
   ```

- Compress your Python code file to a ZIP file
    ```unix
    $ zip lambda.zip lambda_function_square.py
    adding: lambda_function_square.py (deflated 57%)
    ```

- Deploy the Lambda function into the "local stack" AWS infrastructure
  ```unix
  $ awslocal lambda create-function \
  --function-name lambda_function_square \
  --runtime python3.11 \
  --zip-file fileb://lambda.zip \
  --handler lambda_function_square.lambda_handler \
  --role arn:aws:iam::000000000000:role/lambda-role
  ...
      "State": "Pending",
  ...
  ```
  
- Re-deploy the Lambda function if the `zip` file was updated
  ```unix
  $ awslocal lambda update-function-code \
    --function-name lambda_function_square \
    --zip-file fileb://lambda.zip
  ```
  
- Check the status
  ```unix
  $ awslocal lambda get-function --function-name lambda_function_square
  ...
      "State": "Active",
  ...
  ```

- Before using the Lambda function URL, test the function by invoking it directly
  ```unix
  $ awslocal lambda invoke --function-name lambda_function_square \
    --payload '{"number": 6}' output.txt
   {
      "StatusCode": 200,
      "ExecutedVersion": "$LATEST"
   }
  ```

- Check logs
  ```
  $ docker logs localstack
  
  LocalStack version: 4.2.1.dev3
  LocalStack build date: 2025-02-27
  LocalStack build git hash: 3cac1548f
  
  Ready.
  2025-02-27T21:45:39.499  INFO --- [et.reactor-0] localstack.request.aws     : AWS lambda.CreateFunction => 201
  2025-02-27T21:46:04.860  INFO --- [et.reactor-1] localstack.request.aws     : AWS lambda.GetFunction => 200
  2025-02-27T21:46:24.808  INFO --- [et.reactor-0] l.u.container_networking   : Determined main container network: bridge
  2025-02-27T21:46:24.811  INFO --- [et.reactor-0] l.u.container_networking   : Determined main container target IP: 172.17.0.2
  2025-02-27T21:46:25.313  INFO --- [et.reactor-1] localstack.request.http    : POST /_localstack_lambda/bd02d1c6742ba34b9da8ffecd9551a84/status/bd02d1c6742ba34b9da8ffecd9551a84/ready => 202
  2025-02-27T21:46:25.319  INFO --- [et.reactor-1] localstack.request.http    : POST /_localstack_lambda/bd02d1c6742ba34b9da8ffecd9551a84/invocations/fc3806e1-4c91-40d4-ad80-bc6882511933/logs => 202
  2025-02-27T21:46:25.321  INFO --- [et.reactor-1] localstack.request.http    : POST /_localstack_lambda/bd02d1c6742ba34b9da8ffecd9551a84/invocations/fc3806e1-4c91-40d4-ad80-bc6882511933/response => 202
  2025-02-27T21:46:25.324  INFO --- [et.reactor-0] localstack.request.aws     : AWS lambda.Invoke => 200
  ```

- Generate a URL that can be used to invoke the Lambda function
  ```unix
    $ awslocal lambda create-function-url-config \
      --function-name lambda_function_square \
      --auth-type NONE
  {
      "FunctionUrl": "http://9e2fsnh951l3ts5ljyyo38si21fhr341.lambda-url.us-east-1.localhost.localstack.cloud:4566/",
      "FunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:lambda_function_square",
      "AuthType": "NONE",
      "CreationTime": "2025-02-27T21:47:38.944326+0000"
  
    }
  ```

- Trigger the Lambda function URL using **cUrl**
  ```unix
  $ curl -X POST \
      'http://9e2fsnh951l3ts5ljyyo38si21fhr341.lambda-url.us-east-1.localhost.localstack.cloud:4566/' \
      -H 'Content-Type: application/json' \
      -d '{"number": 6}'
    {"result": 36, "event": {"version": "2.0", "routeKey": "$default", "rawPath": "/", "rawQueryString": "", "headers": {"host": "9e2fsnh951l3ts5ljyyo38si21fhr341.lambda-url.us-east-1.localhost.localstack.cloud:4566", "user-agent": "curl/7.81.0", "accept": "*/*", "content-type": "application/json", "content-length": "13", "x-amzn-tls-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256", "x-amzn-tls-version": "TLSv1.2", "x-forwarded-proto": "http", "x-forwarded-for": "", "x-forwarded-port": "4566"}, "queryStringParameters": {}, "requestContext": {"accountId": "anonymous", "apiId": "9e2fsnh951l3ts5ljyyo38si21fhr341", "domainName": "9e2fsnh951l3ts5ljyyo38si21fhr341.lambda-url.us-east-1.localhost.localstack.cloud:4566", "domainPrefix": "9e2fsnh951l3ts5ljyyo38si21fhr341", "http": {"method": "POST", "path": "/", "protocol": "HTTP/1.1", "sourceIp": "", "userAgent": "curl/7.81.0"}, "requestId": "1472a808-0a58-4b07-9cae-066c0e711d15", "routeKey": "$default", "stage": "$default", "time": "27/Feb/2025:22:45:15 +0000", "timeEpoch": 1740696315711}, "body": "{\"number\": 6}", "isBase64Encoded": false}, "type(event)": "<class 'dict'>", "body": {"number": 6}}
  ```

- Stop and remove the running LocalStack container
  ```unix
  $ docker stop localstack
  $ docker rm localstack
  ```
