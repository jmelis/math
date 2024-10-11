IMAGE_NAME = quay.io/jmelis/mathtools:latest

.PHONY: build

build:
	podman build -t $(IMAGE_NAME) .

run:
	podman run -it --rm -p 8000:8000 $(IMAGE_NAME)

debug:
	flask --app app --debug run
