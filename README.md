# Internet Research
Scripts used for Internet Scanning and Research

## Prerequisites
Install the GNU Parallel program. On Debian based systems use `apt-get install parallel`.

Install Masscan using the instructions at https://github.com/robertdavidgraham/masscan

## Parsing Masscan list results
To get the list of IP addresses from the Masscan list results file use the following command:

	grep open ec2_redis.list | cut -d ' ' -f 4 > ips.txt

## Running parallel jobs
The GNU parallel program will read in a file and send each line of the file to the specified program. You can use the --jobs flag to specify the number of jobs to run in parallel.

	parallel --jobs <n> -a <input_file> <path/to/executable> > <result_file>


## Finding Redis Servers
1. Modify the generate_ec2_conf.py file to set the PORT, RATE, and OUTFILE values. To find Redis servers use PORT 6379. At the default rate I can scan all of the EC2 addresses in about an hour. Feel free to increase the rate but be careful because if the rate is too high it will crash your network.
2. Run `masscan -c ec2.conf`. Once the scan is complete parse the output file to get the list of IP addresses with port 6379 open.
3. Use the GNU parallel program to run the redis_check.py script against each address.

## Finding Other Service
1. Create your own script that will take a single IP address as an argument and test whether a specific service is open on a given port.
2. Follow the directions in the Finding Redis Servers section and replace the redis_check.py script in the parallel command with your script.

