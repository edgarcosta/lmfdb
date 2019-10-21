from lmfdb import db
belyi = db.belyi_galmaps
s = ""
#label = '5T4-[5,3,3]-5-311-311-g0-a'
#label = '6T13-[6,4,6]-6-42-321-g1-a'
label = '7T5-[7,7,4]-7-7-421-g2-a'
rec = belyi.lookup(label)
s += "// Magma code for Belyi map with label %s\n\n" % label
s += "// Define the base field\n"
if rec['base_field'] == [-1,1]:
    s += "K<nu> := RationalsAsNumberField();\n"
else:
    s += "R<T> := PolynomialRing(Rationals());\nK<nu> := NumberField(R!%s);\n\n" % rec['base_field']
s += "// Define the curve\n"
if rec['g'] == 0:
    s += "X := Curve(ProjectiveSpace(PolynomialRing(K, 2)));\n"
    s += "// Define the map\n"
    s += "KX<x> := FunctionField(X);\n";
    s += "phi := %s;\n" % rec['map']
elif rec['g'] == 1:
    s += "_<x> := PolynomialRing(K);\n"
    curve_poly = rec['curve'].split("=")[1]   
    s += "X := EllipticCurve(%s);\n" % curve_poly;
    s += "// Define the map\n"
    s += "KX<x,y> := FunctionField(X);\n";
    s += "phi := %s;\n" % rec['map']
elif rec['g'] == 2:
    s += "_<x> := PolynomialRing(K);\n"
    curve_poly = rec['curve'].split("=")[1]   
    s += "X := HyperellipticCurve(%s);\n" % curve_poly; # need to worry about cross-term maybe...
    s += "// Define the map\n"
    s += "KX<x,y> := FunctionField(X);\n";
    s += "phi := %s;\n" % rec['map']
else:
    print("Sorry, not implemented yet! :(")
print(s)
