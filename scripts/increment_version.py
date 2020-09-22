import os
import pkg_resources


if __name__ == "__main__":
    version = pkg_resources\
		.get_distribution("embedded-yaml-docs")\
		.version

    split_version = version.split('.')

	try:
        split_version[-1] = str(int(split_version[-1]) + 1)
    except ValueError:
        # do something about the letters in the last field of version
        pass

	new_version = '.'.join(split_version)

	os.system(f"sed -i \"s/version='[0-9.]\+'/version='{new_version}'/\" setup.py")
    os.system("git add -u")
    os.system(f"git commit -m '[ci skip] Increase version to {new_version}'")
    os.system("git push")
