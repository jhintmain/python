url = "http://naver.com"
star_idx = url.find("//")+2
end_idx = url.find(".")
trim_url = url[star_idx:end_idx]
result_url = trim_url[0:3]+str(len(trim_url))+str(trim_url.count("e"))+"!";
print(result_url)
