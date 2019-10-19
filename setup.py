from setuptools import setup

setup(
    name='MAMoC-Server',
    version='1.0',
    packages=[''],
    url='',
    license='',
    author='Dawand Sulaiman',
    author_email='djs21@st-andrews.ac.uk',
    description='MAMoC Server component for handling WAMP RPC calls and PubSub events. It also uses Androguard '
                'to run a static analysis on APKs and runs a partitioning algorithm on the method call graphs to output'
                'the local and remote partitions of a mobile application',
    install_requires=["six", "txaio", "autobahn", "androguard", "beautifulsoup4", "requests"]  # keep it
    # minimal for offload testing 'networkx', 'metis', 'matplotlib', 'lxml' # This is required packages for the
    # partitioning and graph drawing classes
)
