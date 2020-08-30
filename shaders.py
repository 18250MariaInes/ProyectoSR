from gl import *
"""import numpy as np
from collections import namedtuple

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])
V4 = namedtuple('Point4', ['x', 'y', 'z','w'])"""

#ejemplo de Carlos, base para los hecho por mi
def gouraud(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)
#producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def toon(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)

    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )
    #para gradiente de toon shader, luego todo es igual al gourad
    if (intensity>=0 and intensity<0.3):
        intensity=0
    elif (intensity>=0.3 and intensity<0.5):
        intensity=0.3
    elif (intensity>=0.5 and intensity<0.8):
        intensity=0.5
    elif (intensity>=0.8 and intensity<=1):
        intensity=0.8

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def phong(render, **kwargs):
    Ax, Bx, Cx, Ay, By, Cy, Az, Bz, Cz= kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)
    #producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )
    print(intensity)

    #print(intensity)
    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0

def static(render, **kwargs):

    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)
    #producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )

    #print(intensity)
    b *= intensity
    g *= intensity
    r *= intensity

    prob=random.randint(1,2)
    #print(prob)
    if intensity > 0 and prob==2:
        return r, g, b
    else:
        return 0,0,0

def static_jupiter(render, **kwargs):

    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)
    #producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )

    #print(intensity)
    b *= intensity
    g *= intensity
    r *= intensity

    prob=random.randint(1,4)
    #print(prob)
    if intensity > 0 and prob==2:
        return r, g, b
    elif intensity > 0 and prob==1:
        return r, 0, 0
    elif intensity > 0 and prob==3:
        return 0, g, 0
    elif intensity > 0 and prob==4:
        return 0, 0, b
    else:
        return 0,0,0

def thermal(render, **kwargs):

    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)
    #producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )

    #print(intensity)
    b *= intensity
    g *= intensity
    r *= intensity

    #print(prob)
    if intensity > 0 and intensity <= 0.33 :
        return 0, g, 0
    elif intensity > 0.33 and intensity <= 0.66:
        return r, g, 0
    elif intensity>0.66 and intensity<=1:
        return r,0,b

    else:
        return 0,0,0

def scifi(render, **kwargs):
    Ax, Bx, Cx, Ay, By, Cy, Az, Bz, Cz=kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w
    


    normal = (nx, ny, nz)
#producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )

    b *= intensity
    g *= intensity
    r *= intensity
    #print(render.frobenius(normal))
    if intensity > 0:
        if intensity<0.90:
            return 0,1,0
        return 0, 0, 0
    else:
        return 0,0,0

def stripes(render, **kwargs):
    Ax, Bx, Cx, Ay, By, Cy, Az, Bz, Cz=kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']
    y,x=kwargs['coordy']

    print(y)

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w
    


    normal = (nx, ny, nz)
#producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )

    b *= intensity
    g *= intensity
    r *= intensity
    #print(render.frobenius(normal))
    if intensity > 0:
        if y%50<25:
            return 1,round((y%50)/50),1
        return r,g,b
    else:
        return 0,0,0

def checkered(render, **kwargs):
    Ax, Bx, Cx, Ay, By, Cy, Az, Bz, Cz=kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']
    y,x=kwargs['coordy']

    print(y)

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w

    normal = (nx, ny, nz)
#producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )

    b *= intensity
    g *= intensity
    r *= intensity
    #print(render.frobenius(normal))
    if intensity > 0:
        if y%50<25:
            r,g,b=1,round((y%50)/50),1
            
        if x%50<25:
            r,g,b=round((y%50)/50),1,1
        return r,g,b
    else:
        return 0,0,0
 
 #shader para ejemplo de Carlos
def unlit(render, **kwargs):
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    b, g, r = kwargs['color']

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        texColor = render.active_texture.getColor(tx,ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    return r, g, b

def stripes_neptune(render, **kwargs):
    Ax, Bx, Cx, Ay, By, Cy, Az, Bz, Cz=kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']
    y,x=kwargs['coordy']

    #print(y)

    b /= 255
    g /= 255
    r /= 255

    if render.active_texture:
        tx = tax * u + tbx * v + tcx * w
        ty = tay * u + tby * v + tcy * w
        
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w
    


    normal = (nx, ny, nz)
#producto punto de las funciones que sustituyen a numpy
    intensity = render.dot(normal, render.lightx,render.lighty,render.lightz )

    b *= intensity
    g *= intensity
    r *= intensity
    #print(render.frobenius(normal))
    if intensity > 0:
        if y%15<1:
            return r,g,round((y%50)/50)
        return r,g,b
    else:
        return 0,0,0

#for normal map
def normalMap(render, **kwargs):
    Ax, Bx, Cx, Ay, By, Cy, Az, Bz, Cz=kwargs['verts']
    u, v, w = kwargs['baryCoords']
    tax, tbx, tcx, tay, tby, tcy = kwargs['texCoords']
    na, nb, nc = kwargs['normals']
    b, g, r = kwargs['color']

    """B=V3(Bx, By, Bz)
    A=V3(Ax, Ay, Az)
    C=V3(Cx, Cy, Cz)

    ta=V2(tax, tay)
    tb=V2(tbx, tby)
    tc=V2(tcx, tcy)"""

    b /= 255
    g /= 255
    r /= 255

    tx = tax * u + tbx * v + tcx * w
    ty = tay * u + tby * v + tcy * w

    if render.active_texture:
        texColor = render.active_texture.getColor(tx, ty)
        b *= texColor[0] / 255
        g *= texColor[1] / 255
        r *= texColor[2] / 255

    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    nz = na[2] * u + nb[2] * v + nc[2] * w
    #normal = V3(nx, ny, nz)
    normalp = (nx, ny, nz)

    if render.active_normalMap:
        texNormal = render.active_normalMap.getColor(tx, ty)
        texNormal = [ (texNormal[2] / 255) * 2 - 1,
                      (texNormal[1] / 255) * 2 - 1,
                      (texNormal[0] / 255) * 2 - 1]

        
        texNormal=render.division(texNormal,render.frobenius(texNormal))

        
        edge1p=render.subtract(Bx, Ax, By, Ay, Bz, Az)#funciona
        """print(edge1p)
        print(edge1)
        print("--------------------------------")"""
        
        edge2p=render.subtract(Cx, Ax, Cy, Ay, Cz, Az)#funciona
        """"print(edge2p)
        print(edge2)
        print("--------------------------------")"""
        
        deltaUV1p=render.subtractTwo(tbx, tax, tby, tay)#funciona
        """print(deltaUV1p)
        print(deltaUV1)
        print("--------------------------------")"""
        
        deltaUV2p=render.subtractTwo(tcx, tax, tcy, tay)#funciona
        """print(deltaUV2p)
        print(deltaUV2)
        print("--------------------------------")"""

        tangent = [0,0,0]
        
        
        try:
            fp= 1 / (deltaUV1p[0] * deltaUV2p[1] - deltaUV2p[0] * deltaUV1p[1])
        except:
            fp=1
            pass
        
        """print(fp)
        print("---------------------------------------")"""
        

        tangent[0] = fp * (deltaUV2p[1] * edge1p[0] - deltaUV1p[1] * edge2p[0])
        tangent[1] = fp * (deltaUV2p[1] * edge1p[1] - deltaUV1p[1] * edge2p[1])
        tangent[2] = fp * (deltaUV2p[1] * edge1p[2] - deltaUV1p[1] * edge2p[2])

        
        tangentp=render.division(tangent,render.frobenius(tangent))#funciona
        """print(tangent)
        print(tangentp)
        print("---------------------------------------")"""
        """print(np.dot(tangent, normal))
        print(render.dot(tangentp,nx,ny,nz ))#funciona
        print("---------------------------------------")"""
        """print(np.multiply(render.dot(tangentp,nx,ny,nz ),normal))
        print(render.multiN(render.dot(tangentp,nx,ny,nz),normalp))#funciona
        print("---------------------------------------------------------")"""
        """print(np.subtract(tangent, render.multiN(render.dot(tangentp,nx,ny,nz),normalp)))
        print(np.subtract(tangentp, render.multiN(render.dot(tangentp,nx,ny,nz),normalp)))
        res=render.multiN(render.dot(tangentp,nx,ny,nz),normalp)
        print(render.subtract(tangentp[0],res[0],tangentp[1],res[1],tangentp[2],res[2]))#funciona
        print("------------------------------------------------------------------")"""
        res=render.multiN(render.dot(tangentp,nx,ny,nz),normalp)
        tangent = render.subtract(tangentp[0],res[0],tangentp[1],res[1],tangentp[2],res[2])

        tangent = render.division(tangent,render.frobenius(tangent))

        
        bitangent=render.cross(normalp, tangent)
        
        bitangent=render.division(bitangent,render.frobenius(bitangent))

        #para convertir de espacio global a espacio tangente
        tangentMatrix = [[tangent[0],bitangent[0],normalp[0]],
                                [tangent[1],bitangent[1],normalp[1]],
                                [tangent[2],bitangent[2],normalp[2]]]

        
        lightp=[[render.lightx],[render.lighty],[render.lightz]]
        
        lightp=render.multMaster(tangentMatrix,lightp )
        """print(light)
        print(lightp)
        print("----------------------------------------------------")"""
        light=(lightp[0][0],lightp[1][0],lightp[2][0])
        
        light=render.division(light,render.frobenius(light))

        intensity=render.dot(texNormal, light[0], light[1],light[2])
    else:
        intensity = render.dot(normal, render.lightx,render.lighty,render.lightz)

    b *= intensity
    g *= intensity
    r *= intensity

    if intensity > 0:
        return r, g, b
    else:
        return 0,0,0