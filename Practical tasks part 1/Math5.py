import re


def main(s):
    pattern1 = r"\'\w+\'"
    pattern2 = r"(?<=(list\())([\s\S]+?\;)"
    parsed_s1 = re.findall(pattern1, s.replace('\n', ''))
    parsed_s2 = re.findall(pattern2, s.replace('\n', ''))
    pattern3 = r"(\(\w+\))"
    dict = {}
    for i in range(len(parsed_s1)):
        parsed_s3 = re.findall(pattern3, parsed_s2[i][1].replace('\n', ''))
        for j in range(len(parsed_s3)):
            parsed_s3[j] = parsed_s3[j].lstrip("(").rstrip(")")
        dict[parsed_s1[i].strip("'")] = parsed_s3
    return dict


expr1 = (
    "<sect> <% store 'usried_920'is list( q(dimaza_172) q(maanen_298)) \
%>;<% store 'ladies' is list( q(edis) q(erorer_471) q(inma_662) \
q(edatar_811)) %>; </sect>"
)

print(main(expr1))
