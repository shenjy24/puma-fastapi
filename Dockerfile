FROM continuumio/miniconda3
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml -y
# Pull the environment name out of the environment.yml
RUN echo "source activate $(head -1 /tmp/environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 /tmp/environment.yml | cut -d' ' -f2)/bin:$PATH

# 设置工作目录
WORKDIR /app

# 复制当前目录的所有内容到工作目录
COPY . /app

# 对外暴露端口，FastAPI默认端口为8000
EXPOSE 8000

# 启动FastAPI应用
CMD ["/opt/conda/envs/fastapi/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]