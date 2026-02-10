# A function to create directories
mcd()
{
	mkdir -p "$1"
	cd "$1"
}
