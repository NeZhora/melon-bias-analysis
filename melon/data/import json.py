import json
import csv

def json_to_csv(input_file, output_file, target_year):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    albums = data.get('albums', [])
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['id', 'video_date', 'score', 'name'])
        
        for index, album in enumerate(albums, start=1):
            year = -2
            actual_score = -2
            name = album.get('album_clean', '')
            video_date = album.get('video_date', '')
            
            try:
                year = int(video_date[:4])
            except (ValueError, TypeError):
                video_date = album.get('year', '')
                year = int(video_date[:4])

            if year != target_year and target_year != 0:
                pass
            
            else:
                score = (album.get('score', ''))
                if score == "CLASSIC" or score == "classic":
                    actual_score = 11
                else:
                    try:
                        actual_score = int(score)
                        if not (0 <= actual_score <= 11):
                            actual_score = -1
                    except (ValueError, TypeError):
                        actual_score = -1

                writer.writerow([index, year, actual_score, name])
        
    print(f"CSV успешно создан: {output_file}")

if __name__ == "__main__":

    input_json = "fantano-scores-2026-04-19.json"  
    output_csv = "ALL_fantano-scores-albums.csv"
    json_to_csv(input_json, output_csv, 0) 
    for i in range(2010, 2027):
        output_csv = "by year\\fantano-scores-albums" +str(i)+ ".csv"
        json_to_csv(input_json, output_csv, i)