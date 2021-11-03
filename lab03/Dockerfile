FROM ubuntu:latest

USER root
# Set timezone
RUN ln -snf /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && echo "Etc/UTC" > /etc/timezone 
# Install TeXlive
RUN apt-get update \
    && apt-get install texlive texlive-science -y \
    && apt-get install make -y 
# Go to work directory
RUN mkdir /workspace
WORKDIR /workspace