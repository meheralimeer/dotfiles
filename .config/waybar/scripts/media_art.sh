#!/bin/bash

ART_PATH="/tmp/waybar_album_art.png"
DEFAULT_ART="" # Optional: Path to a default image

# Function to update album art
update_art() {
    url=$(playerctl metadata mpris:artUrl 2>/dev/null)
    
    if [[ -n "$url" ]]; then
        # Handle file:// URIs
        if [[ "$url" == file://* ]]; then
            cp "${url#file://}" "$ART_PATH"
        elif [[ "$url" == http* ]]; then
            curl -s -o "$ART_PATH" "$url"
        fi
    else
        # Clear or set default
        if [[ -n "$DEFAULT_ART" ]]; then
            cp "$DEFAULT_ART" "$ART_PATH"
        else
             rm -f "$ART_PATH"
        fi
    fi
    
    # Signal waybar to reload image (optional, if using signal)
    # pkill -RTMIN+8 waybar 
}

# Listen for changes
playerctl metadata --format '{{ mpris:artUrl }}' -F | while read -r _; do
    update_art
done
