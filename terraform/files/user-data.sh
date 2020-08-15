#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y python3.7 docker python3-pip git vim unzip docker-compose
sudo groupadd docker
sudo usermod -aG docker ${USER}