def Array2Table(data, pixsize):
	q = """
		<style>
			#tabla {{
				border-collapse:collapse;
			}}
			#tabla td, th {{
				padding:0;
				margin:0;
				width:{psize};
				height:{psize};
			}}
		</style>
		<table id='tabla'>
		""".format(psize=pixsize)

	for i in [(data[1:], 'td')]:
		q += "\n".join(
			[
			"<tr>%s</tr>" % str(_mm) 
			for _mm in [
				"".join(
				[
				"<%s style='background-color:%s'></%s>" % (i[1], str(_q), i[1]) 
				for _q in _m
				]
				) for _m in i[0]
			] 
			])
	q += """
		</table>
		"""
	return q