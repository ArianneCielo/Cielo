child: Padding(
  padding: const EdgeInsets.all(16.0),
  child: StreamBuilder<QuerySnapshot>(
    stream: notesCollection.orderBy('created_at', descending: true).snapshots(),
    builder: (context, snapshot) {
      if (snapshot.connectionState == ConnectionState.waiting) {
        return const Center(child: CircularProgressIndicator());
      }
      if (!snapshot.hasData || snapshot.data!.docs.isEmpty) {
        return const Center(child: Text('No notes yet. Create one!'));
      }

      return ListView.builder(
        itemCount: snapshot.data!.docs.length,
        itemBuilder: (context, index) {
          DocumentSnapshot document = snapshot.data!.docs[index];
          String title = document['title'];
          String author = document['author'];
          String content = document['content'];

          return Card(
            child: ListTile(
              title: Text(title),
              subtitle: Text('By: $author\n$content'),
              isThreeLine: true,
            ),
          );
        },
      );
    },
  ),
)