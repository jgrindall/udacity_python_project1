from datetime import datetime
import math

"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.




The `designation` should resolve to a string, the `name` should resolve to either a nonempty string or the value `None`, the `diameter` should resolve to a float (you should use `float('nan')` to represent an undefined diameter), and the `hazardous` flag should resolve to a boolean.

The `approaches` attribute, for now, can be an empty collection. In Task 2, you'll use the real data set to populate this collection with the real `CloseApproach` data.

The `__str__` method that you write is up to you - it'll determine how this object is printed, and should be human-readable. For inspiration, we adopted the following format:

```
>>> neo = ...
>>> print(neo)
NEO {fullname} has a diameter of {diameter:.3f} km and [is/is not] potentially hazardous.
>>> halley = ...
>>> print(halley)
NEO 433 (Eros) has a diameter of 16.840 km and is not potentially hazardous.
```

In the above, `{fullname}` is either `{designation} ({name})` if the `name` exists or simply `{designation}` otherwise. As a hint, this is a great opportunity for a property named `fullname`!


"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, name=None, diameter=float('nan'), hazardous=False):

        """Create a new `NearEarthObject`.
        :param designation: string [required]
        :param name: non-empty string or None
        :diameter designation: float (possibly nan)
        :param hazardous: boolean
        """

        if not designation:
            raise TypeError("Missing designation")
        else:
            self.designation = designation

        self.name = (name if name else None)

        try:
            # diameter must be a float (possibly nan)
            self.diameter = float(diameter)
        except ValueError as error:
            self.diameter = None

        self.hazardous = bool(hazardous)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    def add_approach(self, approach):
        self.approaches.append(approach)

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        pretty_print_name = self.name if self.name else "unnamed"
        return f"{self.designation} ({pretty_print_name})"

    def __str__(self):
        """Return `str(self)`."""
        pretty_print_hazardous = "is potentially hazardous" if self.hazardous else "is not potentially hazardous"
        return f"A NearEarthObject: {self.fullname!r} which has diameter {self.diameter:.3f}km and {pretty_print_hazardous}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")

    @staticmethod
    def fromData(data):
        """static factory method for making a neo from data in json file"""
        designation = data.get('pdes', '')
        name = data.get('name', None)
        diameter = data.get('diameter', float('nan'))
        if not diameter:
            diameter = float('nan')
        pha = data.get('pha', '').upper()
        hazardous = (pha == "Y")
        return NearEarthObject(designation=designation, name=name, diameter=diameter, hazardous=hazardous)


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, time, distance, velocity):
        """Create a new `CloseApproach`.

        :param designation: designation (string, required)
        :param time: time of closest approach to Earth (datetime)
        :param distance: distance of closest approach to Earth in AU (float)
        :param velocity: velocity of closest approach to Earth in km/s (float)

        """

        if not designation:
            raise TypeError("Missing designation")
        else:
            self._designation = designation

        self.time = time if isinstance(time, datetime) else datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def designation(self):
        return self._designation

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """

        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        pretty_print_neo = self.neo.fullname if self.neo else "unknown"
        pretty_print_hazardous = "hazardous" if (self.neo and self.neo.hazardous) else "non-hazardous"
        return (f"A {pretty_print_hazardous} CloseApproach of the object {pretty_print_neo} at time {self.time}, "
                f"at a closest approach distance of {self.distance:.2f}au and a velocity of {self.velocity:.2f}km/s")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")

    def serialize_json(self):
        """

             'datetime_utc', 'distance_au', 'velocity_km_s' to the associated values on the CloseApproach object and the key neo to a dictionary

             mapping the keys 'designation', 'name', 'diameter_km', 'potentially_hazardous' to the associated values on the close approach's NEO.

            As an example, consider the (same) CloseApproach when the NEO Eros approaches Earth on 2025-11-30 02:18. For this close approach, the corresponding entry would be:

            [
              {...},
              {
                "datetime_utc": "2025-11-30 02:18",
                "distance_au": 0.397647483265833,
                "velocity_km_s": 3.72885069167641,
                "neo": {
                  "designation": "433",
                  "name": "Eros",
                  "diameter_km": 16.84,
                  "potentially_hazardous": false
                }
              },
              ...
            ]
            The datetime_utc value should be a string formatted with datetime_to_str from the helpers module; the distance_au and

             velocity_km_s values should be floats; the designation and name should be strings (if the name is missing, it must

             be the empty string); the diameter_km should be a float (if the diameter_km is missing, it should be the JSON value NaN,

             which Python's json loader successfully rehydrates as float('nan')); and potentially_hazardous should be a boolean

              (i.e. the JSON literals false or true, not the strings 'False' nor 'True').
          """

        neo = {
            "designation": self._designation,
            "name": self.neo.name if self.neo.name else "",
            "diameter_km": self.neo.diameter,  # encoded in JSON as NaN if diameter is float('nan')
            "potentially_hazardous": self.neo.hazardous  # encoded in JSON as true/false
        }

        return {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
            "neo": neo
        }

    def serialize_csv(self):

        """As an example, consider the CloseApproach when the NEO Eros approaches Earth on 2025-11-30 02:18. For this close approach, the corresponding row would be:

        datetime_utc,distance_au,velocity_km_s,designation,name,diameter_km,potentially_hazardous
        ...
        2025-11-30 02:18,0.397647483265833,3.72885069167641,433,Eros,16.84,False
        ...
        A missing name must be represented in the CSV output by the empty string (not the string 'None').

         A missing diameter must be represented in the CSV output either by the empty string or by the string 'nan'.

         The potentially_hazardous flag must be represented in the CSV output either by the string 'False' or the string 'True' (not the values 0 or 1, nor the strings 'N' or 'Y').

         """

        return {
            "datetime_utc": self.time_str,
            "distance_au": str(self.distance),
            "velocity_km_s": str(self.velocity),
            "designation": self._designation,
            "name": self.neo.name if self.neo.name else "",
            "diameter_km": "" if math.isnan(self.neo.diameter) else str(self.neo.diameter),
            "potentially_hazardous": "True" if self.neo.hazardous is True else "False"
        }

    @staticmethod
    def fromData(data):
        """static factory method for making a close approach from csv data in file"""
        return CloseApproach(designation=data[0], time=cd_to_datetime(data[3]), distance=float(data[4]), velocity=float(data[7]))
