from haystack import indexes
from grajteka.model import BoardgameMeta

class BoardgameMetaIndex(indexes.SearchIndex, indexes.Indexable):
	title = CharField(document=True, use_template=True)

	def get_model(self):
		return BoardgameMeta

	def index_queryset(self):
		return BoardgameMeta.objects.filter(title=self.title)

