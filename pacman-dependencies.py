from subprocess import check_output

# get list of installed packages
def package_list():
    return check_output(["pacman", "-Qq"]).decode('ascii').splitlines()

# get list of lists of dependencies, one for each package
def dependency_list():
    l = check_output("pacman -Qi|grep Depends|cut -d: -f2", shell=True).decode('ascii').splitlines()

    l = map(str.strip, l)
    l = map(str.split, l)

    return list(l)

packages = package_list()
dependencies = dependency_list()

# each package corresponds to a list of dependencies
# they should be in the same order
assert(len(packages) == len(dependencies))

# associate each package with how many dependencies it has
dep_count = dict(zip(packages, map(len, dependencies)))

top50 = sorted(packages, key=lambda pack:dep_count[pack], reverse=True)[:50]

for package in top50:
    print(package, dep_count[package])
