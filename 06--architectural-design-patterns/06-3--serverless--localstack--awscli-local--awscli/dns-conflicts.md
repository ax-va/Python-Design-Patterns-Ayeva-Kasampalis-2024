# Serverless

## If you have DNS conflicts when using LocalStack

### Explanation

- LocalStack relies on custom DNS settings (especially when binding to `localhost.localstack.cloud`), 
  which `systemd-resolved` might interfere with.
  After stopping `systemd-resolved`, you likely modified `/etc/resolv.conf` manually.

- Restarting `systemd-resolved` reintroduces this conflict.
  If you restart `systemd-resolved`, it may replace `/etc/resolv.conf` with its own configuration,
  potentially breaking LocalStack's DNS resolution.
  
- You stopped `systemd-resolved` to avoid conflicts.
  Since your LocalStack setup modifies DNS (`/etc/resolv.conf`), 
  you stop `systemd-resolved` to prevent conflicts and restart `systemd-networkd` to ensure the new DNS settings apply.

### How to

- Stop and disable `systemd-resolved`, which is responsible for managing DNS resolution 
(i.e., resolving domain names to IP addresses)
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
