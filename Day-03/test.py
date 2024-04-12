# lists is mutable or can be changed [not so good memory footprint]

# you can append and remove from a list not a tuple


s3_bucket_lists = ["kojobucket01", "2024kojobucket", "amazingbuckets124","batmanliveshere"]
s3_bucket_lists.append("diaskfdhsa")
s3_bucket_lists.remove



# tuples are immutable or can not be changed (good memory footprint)
s3_bucket_lists = ("kojobucket01", "2024kojobucket", "amazingbuckets124","batmanliveshere")
print(s3_bucket_lists)

s3_bucket_lists = ("kojobucket01", "2024kojobucket", "amazingbuckets124")
print(type(s3_bucket_lists))