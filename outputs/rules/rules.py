def findDecision(obj): #obj[0]: No, obj[1]: Region, obj[2]: Epicenter, obj[3]: Distance_from_shore, obj[4]: Depth, obj[5]: Scale, obj[6]: Duration
	# {"feature": "Duration", "instances": 15, "metric_value": 0.9183, "depth": 1}
	if obj[6] == ' Long':
		return ' Effect'
	elif obj[6] == ' Short':
		return ' No effect'
	else: return ' No effect'
