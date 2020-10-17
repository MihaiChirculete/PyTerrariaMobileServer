# Pull requests guidelines
Please follow this guideline in order for your pull requests to be elligible to merging. 
  
1. Code submitted in pull requests has to follow PEP8 Guidelines.
2. The package structure from the original code should be reflected in the ported packages structure.  
What this basically means is that for instance if the original code contains a package called `Terraria.IO`,
then our project should contain a package called `terraria.io`   
If a package contains let's say 2 classes like so: `Terraria.IO.FileData` and `Terraria.IO.FileMetadata` then
our project will contain a package `terraria.io` with 2 python files for each of the above classes called
`file_data.py` and `file_metadata.py` and each file will contain the definition of the classes `FileData` and `FileMetadata`
3. Code structure must resemble as much as possible to the original, especially from the functionality point of view.

If all these guidelines are met, feel free to submit your pull request.