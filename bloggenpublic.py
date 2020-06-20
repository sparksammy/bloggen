#Sparksammy's Python3 Static Blog Generator
import glob
blogname = "Your First Blog" #Replace me, then put the posts in the posts/ folder as .txt files.
adcode = '' #Add your AD code here, perferibly with an hr tag preceding it.
copyrightnotice = '<p>Copyright YOURNAMEHERE - All rights reserved.</p>' #Add your copyright notice here.
#Ignore everyting else here unless you know what you are doing.
postsfolder = glob.glob("posts/*.txt")
blog = open("blog.html", "w+")
blog.write('<!DOCTYPE html>')
blog.write('<html>')
blog.write('<head><title>' + blogname + '</title></head>')
blog.write('<body>')
blog.write('<h1>' + blogname + '</h1><hr><a href="index.html">Go home</a> <a href="old-blogs.html">Historic posts</a>')

for filename in postsfolder:
    og = open(filename, "r")
    ogt = og.readline()
    ogc = og.read().replace('\n','').replace(ogt,'')
    blog.write('<hr/>')
    blog.write('<div class="post">')
    blog.write('<h2>' + ogt + '</h2>')
    blog.write('<p>' + ogc + '</p>')
    blog.write('</div>')
    blog.write(adcode);
    og.close()
blog.write('<hr/>')
blog.write(copyrightnotice)
blog.write('</body>')
blog.write('</html>')
blog.close()