def findDecision(obj): #obj[0]: Latitude, obj[1]: Longitude, obj[2]: DepthMeters, obj[3]: MagType, obj[4]: Magnitude, obj[5]: bix_potential_blasts
	# {"feature": "MagType", "instances": 1647, "metric_value": 0.1855, "depth": 1}
	if obj[3] == 'ML':
		# {"feature": "Magnitude", "instances": 1261, "metric_value": 0.0203, "depth": 2}
		if obj[4]<=2.9833189197233754:
			# {"feature": "Latitude", "instances": 1237, "metric_value": 0.0121, "depth": 3}
			if obj[0]<=39.294485044462405:
				# {"feature": "Longitude", "instances": 803, "metric_value": 0.0149, "depth": 4}
				if obj[1]<=-81.65757683686176:
					# {"feature": "DepthMeters", "instances": 452, "metric_value": 0.0061, "depth": 5}
					if obj[2]<=5603.539823008849:
						# {"feature": "bix_potential_blasts", "instances": 261, "metric_value": 0.0006, "depth": 6}
						if obj[5]>0:
							return 1
						elif obj[5]<=0:
							return 1
						else: return 0.75
					elif obj[2]>5603.539823008849:
						# {"feature": "bix_potential_blasts", "instances": 191, "metric_value": 0.002, "depth": 6}
						if obj[5]>0:
							return 1
						elif obj[5]<=0:
							return 1
						else: return 0.5714285714285714
					else: return 0.7696335078534031
				elif obj[1]>-81.65757683686176:
					# {"feature": "bix_potential_blasts", "instances": 351, "metric_value": 0.009, "depth": 5}
					if obj[5]>0:
						# {"feature": "DepthMeters", "instances": 342, "metric_value": 0.0054, "depth": 6}
						if obj[2]<=13033.351154520482:
							return 1
						elif obj[2]>13033.351154520482:
							return 1
						else: return 0.9130434782608695
					elif obj[5]<=0:
						# {"feature": "DepthMeters", "instances": 9, "metric_value": 0.279, "depth": 6}
						if obj[2]<=10700:
							return 1
						elif obj[2]>10700:
							return 0
						else: return 0.25
					else: return 0.6666666666666666
				else: return 0.9487179487179487
			elif obj[0]>39.294485044462405:
				# {"feature": "DepthMeters", "instances": 434, "metric_value": 0.0063, "depth": 4}
				if obj[2]>10017.05069124424:
					# {"feature": "bix_potential_blasts", "instances": 235, "metric_value": 0.0093, "depth": 5}
					if obj[5]>0:
						# {"feature": "Longitude", "instances": 230, "metric_value": 0.0025, "depth": 6}
						if obj[1]<=-73.78874045233226:
							return 1
						elif obj[1]>-73.78874045233226:
							return 1
						else: return 0.6818181818181818
					elif obj[5]<=0:
						# {"feature": "Longitude", "instances": 5, "metric_value": 0.2, "depth": 6}
						if obj[1]>-79.7063:
							return 0
						elif obj[1]<=-79.7063:
							return 1
						else: return 0.5
					else: return 0.2
				elif obj[2]<=10017.05069124424:
					# {"feature": "Longitude", "instances": 199, "metric_value": 0.0069, "depth": 5}
					if obj[1]>-81.35006630993195:
						# {"feature": "bix_potential_blasts", "instances": 197, "metric_value": 0.0, "depth": 6}
						if obj[5]>0:
							return 1
						elif obj[5]<=0:
							return 1
						else: return 0.6666666666666666
					elif obj[1]<=-81.35006630993195:
						return 0
					else: return 0.0
				else: return 0.6532663316582915
			else: return 0.7258064516129032
		elif obj[4]>2.9833189197233754:
			return 0
		else: return 0.0
	elif obj[3] == 'md':
		return 0
	elif obj[3] == 'ml':
		return 0
	elif obj[3] == 'mblg':
		return 0
	elif obj[3] == 'Ml':
		return 0
	elif obj[3] == 'mb':
		return 0
	elif obj[3] == 'lg':
		return 0
	elif obj[3] == 'Md':
		return 0
	elif obj[3] == 'mwr':
		return 0
	elif obj[3] == 'MbLg':
		return 0
	elif obj[3] == 'mwc':
		return 0
	elif obj[3] == 'Mw':
		return 0
	else: return 0.0
