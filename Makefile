IMAGE := ethsrilab/sri-website
CONTAINER := sri-website

#########
# IMAGE #
#########

# build the docker image
.PHONY: docker-image
docker-image: 
	docker build -t $(IMAGE) .

#########
# BUILD #
#########

.PHONY: docker-serve
docker-serve: docker-image
	docker run \
		--rm \
		-v $(shell pwd):/website \
		-p 4000:4000 \
		$(IMAGE) \
		bash -c "bundle add webrick; jekyll serve --trace;"