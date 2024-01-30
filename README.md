# Identeq Coding Challenge

This coding challenge is based on a real problem we've encountered here at IDenteq. We process hundreds of thousands of client addresses, some of which are very well formatted, others not so much!

As part of our address processing, we need to flag addresses that don't have a street name consistent with their postcode. For example try googling *"Devonshire Drive, ST6 4BF"*, you'll see this address doesn't exist, whereas *"Innovation Way, ST6 4BF"* does. We need to filter out addresses that don't have a valid street name consistent with their postcode.

This repo contains two .csv files, **example_input_data.csv** and **example_abp_data.csv**:

 - **example_input_data.csv** contains some typical client input addresses
 - **example_abp_data.csv** contains data from the AddressBase containing all registered addresses for the posctodes that are present in **example_input_data.csv**

Your job is to produce an output .csv file which contains all the data in **example_input_data.csv** plus an extra column called *Street_In_Postcode*. This column should contain *Yes* if the address in that row has a street which is present at that postcode in **example_abp_data.csv**. If the address in that row does not have a street which is present at that postcode in **example_abp_data.csv** then *Street_In_Postcode* which should contain *No*.

**Please follow the steps below:**
1. Fork this repo to your GitHub account
2. Write a script to read in **example_input_data.csv** and **example_abp_data.csv** and create a new file **example_output_data.csv** that contains an extra *Street_In_Postcode* column that flags addresses that have street names that are consistent / inconsistent with their postcode
3. Once you're finished, email the URL of your forked repo to devops@cotportal.co.uk
4. Bonus points for thinking about how to optimise this code for large data sets and how the script could be tested

Good luck!
