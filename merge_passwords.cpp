#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char* argv[]) {
    if(argc < 3) {
        cout << "Usage: " << argv[0] << " output.csv input1.csv input2.csv ..." << endl;
        return 1;
    }
    
    string outputFile = argv[1];
    ofstream out(outputFile);
    if(!out.is_open()){
        cerr << "Cannot open output file." << endl;
        return 1;
    }
    
    bool isFirstFile = true;
    for (int i = 2; i < argc; i++){
        ifstream in(argv[i]);
        if(!in.is_open()){
            cerr << "Cannot open file: " << argv[i] << endl;
            continue;
        }
        string line;
        bool isFirstLine = true;
        while(getline(in, line)) {
            if(isFirstFile) {
                out << line << "\n";
            } else {
                if(isFirstLine) {
                    isFirstLine = false;
                    continue;
                }
                out << line << "\n";
            }
        }
        in.close();
        isFirstFile = false;
    }
    out.close();
    cout << "File merged: " << outputFile << endl;
    return 0;
}
