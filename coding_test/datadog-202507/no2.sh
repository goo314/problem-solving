# 0. (Prerequisite) Sign up Datadog

# 1. Install datadog agent

# 2. Modify configuration file
sudo vim /etc/datadog-agent/datadog.yaml
# Add team, env, hostname, and process_config for Live process monitoring

# 3. Restart and check agent
sudo service datadog-agent restart
sudo service datadog-agent status

# 4. Create custom agent check
sudo vim /etc/datadog-agent/conf.d/my_metric.yaml
# init_config:
# instances:
#   - {}
sudo vim /etc/datadog-agent/checks.d/my_metric.py
# from datadog_checks.base import AgentCheck
# import random

# class MyMetricCheck(AgentCheck):
#     def check(self, instance):
#         value = random.randint(1, 1000)
#         self.gauge("my.metric", value)
