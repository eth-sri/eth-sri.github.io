# Jekyll plugin to automatically wrap room mentions with links to ETH location pages
# This replaces the manual clean_rooms_add_links.py script functionality

Jekyll::Hooks.register :site, :post_render do |site|
  # Room regex pattern matching the Python script logic
  # Matches formats like: CAB G 56, CAB G56, HG F 81.1, HG F81.1
  room_regex = /(?<!\>)(?<space>\s+|\(\s*|,\s*)(?<building>[A-Z]+)\s(?<floor>[A-Z])\s?(?<room>\d+(?:\.\d+)?)/

  site.pages.each do |page|
    if page.output_ext == '.html'
      original_content = page.output
      modified_content = original_content.gsub(room_regex) do |match|
        space = $~[:space]
        building = $~[:building]
        floor = $~[:floor]
        room = $~[:room]
        
        # Create the ETH location link
        link_url = "https://ethz.ch/en/utils/location.html?building=#{building}&floor=#{floor}&room=#{room}&lang=en"
        room_text = "#{building} #{floor} #{room}"
        
        "#{space}<a href=\"#{link_url}\">#{room_text}</a>"
      end
      
      # Only update if content was modified
      if original_content != modified_content
        page.output = modified_content
        Jekyll.logger.info "Room Links:", "Added room links to #{page.path}"
      end
    end
  end

  # Also process documents from collections
  site.collections.each do |name, collection|
    collection.docs.each do |doc|
      if doc.output_ext == '.html'
        original_content = doc.output
        modified_content = original_content.gsub(room_regex) do |match|
          space = $~[:space]
          building = $~[:building]
          floor = $~[:floor]
          room = $~[:room]
          
          # Create the ETH location link
          link_url = "https://ethz.ch/en/utils/location.html?building=#{building}&floor=#{floor}&room=#{room}&lang=en"
          room_text = "#{building} #{floor} #{room}"
          
          "#{space}<a href=\"#{link_url}\">#{room_text}</a>"
        end
        
        # Only update if content was modified
        if original_content != modified_content
          doc.output = modified_content
          Jekyll.logger.info "Room Links:", "Added room links to #{doc.relative_path}"
        end
      end
    end
  end
end
