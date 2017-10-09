![status: active](https://img.shields.io/badge/status-active-green.svg)


# tonylin.profile.aws

To build my personal profile on python and flask standing on AWS ElasticBeanstalk , also it's an experiment to compare the difference between deploying/write same code for AWS/GCP

## Rquired Use Case (GCP / AWS)

- [ ] A landing page using bootstrap
- [ ] Embed linkedin widet on the landing page
- [ ] Add a tech section to experiement on new stuff  
- [ ] and more ...

## Optional Feature

- [ ] Support for Google Search Console 
- [x] add [2017_api_traffic_demo] page and add SocketIO Server to listen realtime api traffics
- [x] on [2017_api_traffic_demo] page that visualize the api traffics using sankey diagram (the sankey diagram come from reference section)
- [ ] Integrate with LinkedIn API to retrive my working experiences

## Fuctional feature (will protomote to Use Case Section after completion)

- [x] Use boto (a python package) to access S3 bucket
- [x] keen.io : event streaming and collecting
- [] 


## something worth to memo while experimenting

- [x] Understand .ebextensions like configuration management feature to customize environment declaratively  
- [x] Protect IAM key/secret using **eb setenv (or software configuration in environment variable section) **, then access env variable in python code
- [x] requirements.txt only work after **git push** then eb deploy 

## References

[python 2.7]
[data-flow-graph](https://github.com/macbre/data-flow-graph/blob/master/docs/index.html) is a great candidate for visualize api traffic
[sankey diagram](http://bl.ocks.org/cfergus/raw/3956043/)
[Flask-OAuthlib](https://github.com/lepture/flask-oauthlib)


## Very cool stuff to study
[Bear 71](https://github.com/nfbinteractive/Bear71VR_OpenSource)

