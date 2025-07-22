# Jekyll plugin to automatically wrap room mentions with links to ETH location pages
# This replaces the manual clean_rooms_add_links.py script functionality

Jekyll::Hooks.register :site, :post_render do |site|
  # Room regex pattern matching the Python script logic
  # Matches formats like: CAB G 56, CAB G56, HG F 81.1, HG F81.1
  room_regex = /(?<space>\s+|\(\s*|,\s*|>)(?<building>[A-Z]+)\s(?<floor>[A-Z])\s?(?<room>\d+(?:\.\d+)?)(?<endspace>\s*)/
  Jekyll.logger.info "Room Links:", "Adding room links"

  # Helper method to process room links in content
  def process_room_links(content, regex)
    content.gsub(regex) do |match|
      space = $~[:space]
      building = $~[:building]
      floor = $~[:floor]
      room = $~[:room]
      endspace = $~[:endspace]
      
      # Create the ETH location link
      link_url = "https://ethz.ch/en/utils/location.html?building=#{building}&floor=#{floor}&room=#{room}&lang=en"
      room_text = "#{building} #{floor} #{room}"
      
      space.gsub!(/\s+/, "&nbsp;")
      endspace.gsub!(/\s+/, "&nbsp;")
      "#{space}<a href=\"#{link_url}\">#{room_text}</a>#{endspace}"
    end
  end

  # Collect all HTML documents (pages and collection documents)
  all_documents = site.pages.select { |page| page.output_ext == '.html' }
  
  site.collections.each do |name, collection|
    all_documents.concat(collection.docs.select { |doc| doc.output_ext == '.html' })
  end

  # Process all documents in a unified loop
  all_documents.each do |document|
    original_content = document.output
    modified_content = process_room_links(original_content, room_regex)
    
    # Only update if content was modified
    if original_content != modified_content
      document.output = modified_content
    end
  end
end
