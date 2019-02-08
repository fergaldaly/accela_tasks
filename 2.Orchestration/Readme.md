# Cloudformation Template

Creates a VPC with single Linux/Apache/PHP webserver at the frontend, back by a dual-AZ RDS MySQL instance.

A more robust production setup would at least utilise a load-balancer across multiple AZs, including autoscaling if the application was expected to see wide variations in traffic.

##### Gotchas
- In this example, SSH is not open, you will need to modify the security group after creation if you wish to SSH onto it
- On the parameter selection screen you must select two **different** AZs for the RDS Subnets. Creation will fail otherwise
   - I'm sure it's possible to put validation rules in place to prevent this
- RDS Instance can take 15-20 minutes to create. (*This made testing & verification very annoying!*)

##### Outputs
The template will provide the URL of the Webserver as well the hostname of the RDS instance (for troubleshooting!)
