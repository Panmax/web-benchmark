> 为了做性能测试临时用一下


### usage

```bash
docker build -t panmax/docker-flask .
docker run -d --name docker-flask --restart=always -p 5000:5000 panmax/docker-flask
```