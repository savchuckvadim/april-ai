# import runpod
# from deploy.config import POD_CONF, GPU_COUNT

# def deploy_llm(model_id=None):
#     pod_conf=POD_CONF
#     if model_id:
#         pod_conf.update({
#             "docker_args": f"--model-id {model_id} --num-shard {GPU_COUNT}",
#         })

#     runpod.create_pod(**pod_conf)    