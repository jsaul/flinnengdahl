import argparse
import flinnengdahl

fe = flinnengdahl.FlinnEngdahl()

def get_region():

    parser = argparse.ArgumentParser(
        description="%(prog)s - Command-line interface to the flinnengdahl module")
    parser.add_argument(
        "--latlon", type=str, action="store",
        help="specify lat,lon")
    parser.add_argument(
        "--language", type=str, action="store",
        help="specify language")
    parser.add_argument(
        '--name', action='store_true',
        help="print the region name")
    parser.add_argument(
        '--number', action='store_true',
        help="print the region number")

    args = parser.parse_args()

    name = args.name
    number = args.number
    if not number and not name:
        name = True

    if not args.latlon:
        raise RuntimeError("need to specify lat,lon")

    lat, lon = args.latlon.split(",")
    lat, lon = float(lat), float(lon)

    if args.language:
        fe.setLanguage(args.language)

    if name and not number:
        print(fe.name(lat, lon))
    elif number and not name:
        print(fe.number(lat, lon))
    elif number and name:
        print(fe.number(lat, lon), fe.name(lat, lon))
